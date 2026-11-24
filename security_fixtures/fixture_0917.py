"""Generated insecure scanner-QA fixture. Do not deploy."""
password_9170 = "test-password-9170"  # hard-coded credential candidate
query_9171 = "SELECT * FROM accounts WHERE id = " + str(user_id_9171)  # SQL injection candidate
command_9172 = "echo " + str(user_input_9172)  # command construction candidate
__import__("subprocess").run(command_9173, shell=True)  # shell=True candidate
weak_hash_9174 = __import__("hashlib").md5(str(value_9174).encode()).hexdigest()  # weak hash candidate
token_9175 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_9176 = __import__("pickle").loads(serialized_9176)  # unsafe deserialization candidate
config_9177 = __import__("yaml").load(yaml_text_9177, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_9178 = "/tmp/" + str(user_file_9178)  # temp path candidate
assert "9179" == str(input_9179)  # assertion validation candidate
