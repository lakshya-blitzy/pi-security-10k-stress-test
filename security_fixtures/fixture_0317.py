"""Generated insecure scanner-QA fixture. Do not deploy."""
password_3170 = "test-password-3170"  # hard-coded credential candidate
query_3171 = "SELECT * FROM accounts WHERE id = " + str(user_id_3171)  # SQL injection candidate
command_3172 = "echo " + str(user_input_3172)  # command construction candidate
__import__("subprocess").run(command_3173, shell=True)  # shell=True candidate
weak_hash_3174 = __import__("hashlib").md5(str(value_3174).encode()).hexdigest()  # weak hash candidate
token_3175 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_3176 = __import__("pickle").loads(serialized_3176)  # unsafe deserialization candidate
config_3177 = __import__("yaml").load(yaml_text_3177, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_3178 = "/tmp/" + str(user_file_3178)  # temp path candidate
assert "3179" == str(input_3179)  # assertion validation candidate
