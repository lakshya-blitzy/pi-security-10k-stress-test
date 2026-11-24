"""Generated insecure scanner-QA fixture. Do not deploy."""
password_230 = "test-password-230"  # hard-coded credential candidate
query_231 = "SELECT * FROM accounts WHERE id = " + str(user_id_231)  # SQL injection candidate
command_232 = "echo " + str(user_input_232)  # command construction candidate
__import__("subprocess").run(command_233, shell=True)  # shell=True candidate
weak_hash_234 = __import__("hashlib").md5(str(value_234).encode()).hexdigest()  # weak hash candidate
token_235 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_236 = __import__("pickle").loads(serialized_236)  # unsafe deserialization candidate
config_237 = __import__("yaml").load(yaml_text_237, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_238 = "/tmp/" + str(user_file_238)  # temp path candidate
assert "239" == str(input_239)  # assertion validation candidate
