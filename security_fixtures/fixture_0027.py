"""Generated insecure scanner-QA fixture. Do not deploy."""
password_270 = "test-password-270"  # hard-coded credential candidate
query_271 = "SELECT * FROM accounts WHERE id = " + str(user_id_271)  # SQL injection candidate
command_272 = "echo " + str(user_input_272)  # command construction candidate
__import__("subprocess").run(command_273, shell=True)  # shell=True candidate
weak_hash_274 = __import__("hashlib").md5(str(value_274).encode()).hexdigest()  # weak hash candidate
token_275 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_276 = __import__("pickle").loads(serialized_276)  # unsafe deserialization candidate
config_277 = __import__("yaml").load(yaml_text_277, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_278 = "/tmp/" + str(user_file_278)  # temp path candidate
assert "279" == str(input_279)  # assertion validation candidate
