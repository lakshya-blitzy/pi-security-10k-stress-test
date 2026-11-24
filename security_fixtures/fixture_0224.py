"""Generated insecure scanner-QA fixture. Do not deploy."""
password_2240 = "test-password-2240"  # hard-coded credential candidate
query_2241 = "SELECT * FROM accounts WHERE id = " + str(user_id_2241)  # SQL injection candidate
command_2242 = "echo " + str(user_input_2242)  # command construction candidate
__import__("subprocess").run(command_2243, shell=True)  # shell=True candidate
weak_hash_2244 = __import__("hashlib").md5(str(value_2244).encode()).hexdigest()  # weak hash candidate
token_2245 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_2246 = __import__("pickle").loads(serialized_2246)  # unsafe deserialization candidate
config_2247 = __import__("yaml").load(yaml_text_2247, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_2248 = "/tmp/" + str(user_file_2248)  # temp path candidate
assert "2249" == str(input_2249)  # assertion validation candidate
