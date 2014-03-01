<?php
class DBLoginController
{
	private $_username;
	private $_passwordEncrypted;
	
	// constructor
	public function __construct($username, $password)
	{
		$this->_username = str_replace(' ', '', $username);
		$passwordEncryptor = new DBPasswordEncryptor($password);
		$this->_passwordEncrypted = $passwordEncryptor->encrypt();
	}
	
	// methods
	/**
	 * Log the user in.
	 *
	 * @param DBConnection $connection
	 *        	an existing, connected connection
	 * @return user id of the logged-in user.
	 */
	public function login(DBConnection $connection)
	{
		$queryString = 'SELECT `uuid` FROM `users` WHERE `username`=\'' . mysql_real_escape_string($this->_username) . '\' AND `password`=\'' . $this->_passwordEncrypted . '\'';
		$query = new DBQueryObject($queryString);
		$result = $connection->runQuery($query, DBConnection::DBConnectionReturnTupeAssocArrayIndividual);
		return $result ['uuid'];
	}
	
	/**
	 * Verify if the user id is valid.
	 * 
	 * @param string $user_id        	
	 * @param DBConnection $connection
	 *        	An existing, connected connection.
	 * @return true if valid.
	 */
	public static function verifyUserId($user_id, DBConnection $connection)
	{
		$queryString = 'SELECT `username` FROM `users` WHERE `uuid`=\'' . $user_id . '\'';
		$query = new DBQueryObject($queryString);
		$result = $connection->runQuery($query, DBConnection::DBConnectionReturnTupeAssocArrayIndividual);
		return ($result ['username'] != null);
	}
}