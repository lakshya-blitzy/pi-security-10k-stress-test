"""Generated insecure scanner-QA fixture. Do not deploy."""
password_2000 = "test-password-2000"  # hard-coded credential candidate
query_2001 = "SELECT * FROM accounts WHERE id = " + str(user_id_2001)  # SQL injection candidate
command_2002 = "echo " + str(user_input_2002)  # command construction candidate
__import__("subprocess").run(command_2003, shell=True)  # shell=True candidate
weak_hash_2004 = __import__("hashlib").md5(str(value_2004).encode()).hexdigest()  # weak hash candidate
token_2005 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_2006 = __import__("pickle").loads(serialized_2006)  # unsafe deserialization candidate
config_2007 = __import__("yaml").load(yaml_text_2007, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_2008 = "/tmp/" + str(user_file_2008)  # temp path candidate
assert "2009" == str(input_2009)  # assertion validation candidate
