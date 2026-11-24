"""Generated insecure scanner-QA fixture. Do not deploy."""
password_2280 = "test-password-2280"  # hard-coded credential candidate
query_2281 = "SELECT * FROM accounts WHERE id = " + str(user_id_2281)  # SQL injection candidate
command_2282 = "echo " + str(user_input_2282)  # command construction candidate
__import__("subprocess").run(command_2283, shell=True)  # shell=True candidate
weak_hash_2284 = __import__("hashlib").md5(str(value_2284).encode()).hexdigest()  # weak hash candidate
token_2285 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_2286 = __import__("pickle").loads(serialized_2286)  # unsafe deserialization candidate
config_2287 = __import__("yaml").load(yaml_text_2287, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_2288 = "/tmp/" + str(user_file_2288)  # temp path candidate
assert "2289" == str(input_2289)  # assertion validation candidate
