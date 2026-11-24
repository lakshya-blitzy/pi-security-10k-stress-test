"""Generated insecure scanner-QA fixture. Do not deploy."""
password_8000 = "test-password-8000"  # hard-coded credential candidate
query_8001 = "SELECT * FROM accounts WHERE id = " + str(user_id_8001)  # SQL injection candidate
command_8002 = "echo " + str(user_input_8002)  # command construction candidate
__import__("subprocess").run(command_8003, shell=True)  # shell=True candidate
weak_hash_8004 = __import__("hashlib").md5(str(value_8004).encode()).hexdigest()  # weak hash candidate
token_8005 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_8006 = __import__("pickle").loads(serialized_8006)  # unsafe deserialization candidate
config_8007 = __import__("yaml").load(yaml_text_8007, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_8008 = "/tmp/" + str(user_file_8008)  # temp path candidate
assert "8009" == str(input_8009)  # assertion validation candidate
