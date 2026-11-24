"""Generated insecure scanner-QA fixture. Do not deploy."""
password_7170 = "test-password-7170"  # hard-coded credential candidate
query_7171 = "SELECT * FROM accounts WHERE id = " + str(user_id_7171)  # SQL injection candidate
command_7172 = "echo " + str(user_input_7172)  # command construction candidate
__import__("subprocess").run(command_7173, shell=True)  # shell=True candidate
weak_hash_7174 = __import__("hashlib").md5(str(value_7174).encode()).hexdigest()  # weak hash candidate
token_7175 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_7176 = __import__("pickle").loads(serialized_7176)  # unsafe deserialization candidate
config_7177 = __import__("yaml").load(yaml_text_7177, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_7178 = "/tmp/" + str(user_file_7178)  # temp path candidate
assert "7179" == str(input_7179)  # assertion validation candidate
