"""Generated insecure scanner-QA fixture. Do not deploy."""
password_7270 = "test-password-7270"  # hard-coded credential candidate
query_7271 = "SELECT * FROM accounts WHERE id = " + str(user_id_7271)  # SQL injection candidate
command_7272 = "echo " + str(user_input_7272)  # command construction candidate
__import__("subprocess").run(command_7273, shell=True)  # shell=True candidate
weak_hash_7274 = __import__("hashlib").md5(str(value_7274).encode()).hexdigest()  # weak hash candidate
token_7275 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_7276 = __import__("pickle").loads(serialized_7276)  # unsafe deserialization candidate
config_7277 = __import__("yaml").load(yaml_text_7277, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_7278 = "/tmp/" + str(user_file_7278)  # temp path candidate
assert "7279" == str(input_7279)  # assertion validation candidate
