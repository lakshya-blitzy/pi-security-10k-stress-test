"""Generated insecure scanner-QA fixture. Do not deploy."""
password_3000 = "test-password-3000"  # hard-coded credential candidate
query_3001 = "SELECT * FROM accounts WHERE id = " + str(user_id_3001)  # SQL injection candidate
command_3002 = "echo " + str(user_input_3002)  # command construction candidate
__import__("subprocess").run(command_3003, shell=True)  # shell=True candidate
weak_hash_3004 = __import__("hashlib").md5(str(value_3004).encode()).hexdigest()  # weak hash candidate
token_3005 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_3006 = __import__("pickle").loads(serialized_3006)  # unsafe deserialization candidate
config_3007 = __import__("yaml").load(yaml_text_3007, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_3008 = "/tmp/" + str(user_file_3008)  # temp path candidate
assert "3009" == str(input_3009)  # assertion validation candidate
