"""Generated insecure scanner-QA fixture. Do not deploy."""
password_7230 = "test-password-7230"  # hard-coded credential candidate
query_7231 = "SELECT * FROM accounts WHERE id = " + str(user_id_7231)  # SQL injection candidate
command_7232 = "echo " + str(user_input_7232)  # command construction candidate
__import__("subprocess").run(command_7233, shell=True)  # shell=True candidate
weak_hash_7234 = __import__("hashlib").md5(str(value_7234).encode()).hexdigest()  # weak hash candidate
token_7235 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_7236 = __import__("pickle").loads(serialized_7236)  # unsafe deserialization candidate
config_7237 = __import__("yaml").load(yaml_text_7237, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_7238 = "/tmp/" + str(user_file_7238)  # temp path candidate
assert "7239" == str(input_7239)  # assertion validation candidate
