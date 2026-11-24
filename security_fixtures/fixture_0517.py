"""Generated insecure scanner-QA fixture. Do not deploy."""
password_5170 = "test-password-5170"  # hard-coded credential candidate
query_5171 = "SELECT * FROM accounts WHERE id = " + str(user_id_5171)  # SQL injection candidate
command_5172 = "echo " + str(user_input_5172)  # command construction candidate
__import__("subprocess").run(command_5173, shell=True)  # shell=True candidate
weak_hash_5174 = __import__("hashlib").md5(str(value_5174).encode()).hexdigest()  # weak hash candidate
token_5175 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_5176 = __import__("pickle").loads(serialized_5176)  # unsafe deserialization candidate
config_5177 = __import__("yaml").load(yaml_text_5177, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_5178 = "/tmp/" + str(user_file_5178)  # temp path candidate
assert "5179" == str(input_5179)  # assertion validation candidate
