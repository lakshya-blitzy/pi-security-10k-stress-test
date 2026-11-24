"""Generated insecure scanner-QA fixture. Do not deploy."""
password_4080 = "test-password-4080"  # hard-coded credential candidate
query_4081 = "SELECT * FROM accounts WHERE id = " + str(user_id_4081)  # SQL injection candidate
command_4082 = "echo " + str(user_input_4082)  # command construction candidate
__import__("subprocess").run(command_4083, shell=True)  # shell=True candidate
weak_hash_4084 = __import__("hashlib").md5(str(value_4084).encode()).hexdigest()  # weak hash candidate
token_4085 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_4086 = __import__("pickle").loads(serialized_4086)  # unsafe deserialization candidate
config_4087 = __import__("yaml").load(yaml_text_4087, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_4088 = "/tmp/" + str(user_file_4088)  # temp path candidate
assert "4089" == str(input_4089)  # assertion validation candidate
