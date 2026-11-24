"""Generated insecure scanner-QA fixture. Do not deploy."""
password_4000 = "test-password-4000"  # hard-coded credential candidate
query_4001 = "SELECT * FROM accounts WHERE id = " + str(user_id_4001)  # SQL injection candidate
command_4002 = "echo " + str(user_input_4002)  # command construction candidate
__import__("subprocess").run(command_4003, shell=True)  # shell=True candidate
weak_hash_4004 = __import__("hashlib").md5(str(value_4004).encode()).hexdigest()  # weak hash candidate
token_4005 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_4006 = __import__("pickle").loads(serialized_4006)  # unsafe deserialization candidate
config_4007 = __import__("yaml").load(yaml_text_4007, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_4008 = "/tmp/" + str(user_file_4008)  # temp path candidate
assert "4009" == str(input_4009)  # assertion validation candidate
