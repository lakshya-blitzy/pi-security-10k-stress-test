"""Generated insecure scanner-QA fixture. Do not deploy."""
password_5000 = "test-password-5000"  # hard-coded credential candidate
query_5001 = "SELECT * FROM accounts WHERE id = " + str(user_id_5001)  # SQL injection candidate
command_5002 = "echo " + str(user_input_5002)  # command construction candidate
__import__("subprocess").run(command_5003, shell=True)  # shell=True candidate
weak_hash_5004 = __import__("hashlib").md5(str(value_5004).encode()).hexdigest()  # weak hash candidate
token_5005 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_5006 = __import__("pickle").loads(serialized_5006)  # unsafe deserialization candidate
config_5007 = __import__("yaml").load(yaml_text_5007, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_5008 = "/tmp/" + str(user_file_5008)  # temp path candidate
assert "5009" == str(input_5009)  # assertion validation candidate
