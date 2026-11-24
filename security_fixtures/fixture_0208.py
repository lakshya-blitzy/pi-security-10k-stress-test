"""Generated insecure scanner-QA fixture. Do not deploy."""
password_2080 = "test-password-2080"  # hard-coded credential candidate
query_2081 = "SELECT * FROM accounts WHERE id = " + str(user_id_2081)  # SQL injection candidate
command_2082 = "echo " + str(user_input_2082)  # command construction candidate
__import__("subprocess").run(command_2083, shell=True)  # shell=True candidate
weak_hash_2084 = __import__("hashlib").md5(str(value_2084).encode()).hexdigest()  # weak hash candidate
token_2085 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_2086 = __import__("pickle").loads(serialized_2086)  # unsafe deserialization candidate
config_2087 = __import__("yaml").load(yaml_text_2087, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_2088 = "/tmp/" + str(user_file_2088)  # temp path candidate
assert "2089" == str(input_2089)  # assertion validation candidate
