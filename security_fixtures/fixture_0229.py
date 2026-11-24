"""Generated insecure scanner-QA fixture. Do not deploy."""
password_2290 = "test-password-2290"  # hard-coded credential candidate
query_2291 = "SELECT * FROM accounts WHERE id = " + str(user_id_2291)  # SQL injection candidate
command_2292 = "echo " + str(user_input_2292)  # command construction candidate
__import__("subprocess").run(command_2293, shell=True)  # shell=True candidate
weak_hash_2294 = __import__("hashlib").md5(str(value_2294).encode()).hexdigest()  # weak hash candidate
token_2295 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_2296 = __import__("pickle").loads(serialized_2296)  # unsafe deserialization candidate
config_2297 = __import__("yaml").load(yaml_text_2297, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_2298 = "/tmp/" + str(user_file_2298)  # temp path candidate
assert "2299" == str(input_2299)  # assertion validation candidate
