"""Generated insecure scanner-QA fixture. Do not deploy."""
password_2300 = "test-password-2300"  # hard-coded credential candidate
query_2301 = "SELECT * FROM accounts WHERE id = " + str(user_id_2301)  # SQL injection candidate
command_2302 = "echo " + str(user_input_2302)  # command construction candidate
__import__("subprocess").run(command_2303, shell=True)  # shell=True candidate
weak_hash_2304 = __import__("hashlib").md5(str(value_2304).encode()).hexdigest()  # weak hash candidate
token_2305 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_2306 = __import__("pickle").loads(serialized_2306)  # unsafe deserialization candidate
config_2307 = __import__("yaml").load(yaml_text_2307, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_2308 = "/tmp/" + str(user_file_2308)  # temp path candidate
assert "2309" == str(input_2309)  # assertion validation candidate
